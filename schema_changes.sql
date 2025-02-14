-- Create the 'projects' table if it doesn't exist
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Add 'budget' column to the 'projects' table if it doesn't exist
ALTER TABLE projects ADD COLUMN budget DECIMAL(10,2);