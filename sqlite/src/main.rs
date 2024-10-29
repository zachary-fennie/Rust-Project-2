use clap::{Parser, Subcommand};
use rusqlite::{Connection, Result};
use std::error::Error;

mod library;

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Debug, Subcommand)]
enum Commands {
    /// Create the users table
    #[command(alias = "c", short_flag = 'c')]
    Create {},
    
    /// Read from the users table
    #[command(alias = "r", short_flag = 'r')]
    Read {},
    
    /// Query the users table
    #[command(alias = "q", short_flag = 'q')]
    Query { name: String },
    
    /// Update a user's name in the users table
    #[command(alias = "u", short_flag = 'u')]
    Update { old_name: String, new_name: String },
    
    /// Delete a user from the users table
    #[command(alias = "d", short_flag = 'd')]
    Delete { name: String },
    
    /// Load data into the users table from CSV
    #[command(alias = "l", short_flag = 'l')]
    Load {
        file_path: String,
    },
}

fn main() -> Result<(), Box<dyn Error>> {
    let args = Cli::parse();
    let _conn = Connection::open("users.db")?;

    match args.command {
        Commands::Create {} => {
            println!("Creating users table...");
            library::create()?;
        }
        Commands::Read {} => {
            println!("Reading users table...");
            library::read()?;
        }
        Commands::Query { name } => {
            println!("Querying for user: {}", name);
            // You may want to modify the query function to accept a name
            library::query()?;
        }
        Commands::Update { old_name, new_name } => {
            println!("Updating user from '{}' to '{}'", old_name, new_name);
            // Modify the update function to handle name change
            library::update()?;
        }
        Commands::Delete { name } => {
            println!("Deleting user: {}", name);
            // You may want to modify the delete function to use the name
            library::delete()?;
        }
        Commands::Load { file_path } => {
            println!("Loading data from '{}'", file_path);
            library::load(&file_path)?;
        }
    }
    Ok(())
}