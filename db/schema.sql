-- BASED ON SQLite3 type 'affinity' convention
DROP TABLE IF EXISTS source_files;
CREATE TABLE source_files (
	username TEXT, 
	filename TEXT, 
	file_path TEXT,
	file_size_in_bytes INTEGER,
	image_modified_date NUMERIC, 
	UNIQUE (username, filename) ON CONFLICT REPLACE
);
