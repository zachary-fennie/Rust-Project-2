use rusqlite::{params, Connection, Result};
use std::error::Error;
use std::fs::File;
use csv::ReaderBuilder;

pub fn load(dataset: &str) -> Result<&'static str, Box<dyn Error>> {
    println!("Transforming and loading data...");
    println!("Current directory: {:?}", std::env::current_dir());

    // Open the CSV file
    let file = File::open(dataset)?;
    
    // Create a CSV reader from the file
    let mut reader = ReaderBuilder::new()
        .has_headers(true)
        .from_reader(file);

    let conn = Connection::open("users.db")?;
    conn.execute("DROP TABLE IF EXISTS users", [])?;
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        )",
        [],
    )?;

    // Insert data into database
    for result in reader.records() {
        let record = result.map_err(|e| {
            eprintln!("Error reading record: {}", e);
            Box::new(e) as Box<dyn Error>
        })?;
        
        conn.execute(
            "INSERT INTO users (id, name, email, age) VALUES (?1, ?2, ?3, ?4)",
            params![
                record[0].parse::<i32>()?,
                record[1].to_string(),
                record[2].to_string(),
                record[3].parse::<i32>()?
            ],
        )?;
    }

    Ok("users.db")
}


pub fn create() -> Result<&'static str> {
    let conn = Connection::open("users.db")?;
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        )",
        [],
    )?;
    Ok("Create Success")
}

pub fn read() -> Result<&'static str> {
    let conn = Connection::open("users.db")?;
    println!("Top 5 rows of the table:");
    let mut stmt = conn.prepare("SELECT * FROM users LIMIT 5;")?;
    let rows = stmt.query_map([], |row| {
        Ok((
            row.get::<_, i32>(0)?,
            row.get::<_, String>(1)?,
            row.get::<_, String>(2)?,
            row.get::<_, i32>(3)?,
        ))
    })?;

    for row in rows {
        println!("{:?}", row?);
    }
    Ok("Read Success")
}

pub fn query() -> Result<&'static str> {
    let conn = Connection::open("users.db")?;
    println!("Querying data...");
    let mut stmt = conn.prepare("SELECT * FROM users WHERE name = 'Zachary Carter';")?;
    let rows = stmt.query_map([], |row| {
        Ok((
            row.get::<_, i32>(0)?,
            row.get::<_, String>(1)?,
            row.get::<_, String>(2)?,
            row.get::<_, i32>(3)?,
        ))
    })?;

    for row in rows {
        println!("{:?}", row?);
    }
    Ok("Query Success")
}

pub fn update() -> Result<&'static str> {
    let conn = Connection::open("users.db")?;
    conn.execute(
        "UPDATE users SET name = 'Zachary Carter' WHERE name = 'Zachar Carter'",
        [],
    )?;
    Ok("Update Success")
}

pub fn delete() -> Result<&'static str> {
    let conn = Connection::open("users.db")?;
    conn.execute("DELETE FROM users WHERE name = 'Zachary Carter'", [])?;
    Ok("Delete Success")
}

pub fn full_crudquery() -> Result<Vec<&'static str>> {
    let mut results = Vec::new();
    results.push(create()?);
    results.push(read()?);
    results.push(query()?);
    results.push(update()?);
    results.push(delete()?);
    Ok(results)
}

pub fn main() -> Result<(), Box<dyn Error>> {
    let dataset = "sample_data.csv";

    // Load data into the database
    load(dataset)?;

    // Run full CRUD operations
    let results = full_crudquery()?;
    for result in results {
        println!("{}", result);
    }

    Ok(())
}