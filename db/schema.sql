-- BASED ON SQLite3 type 'affinity' convention
DROP TABLE IF EXISTS source_files;
CREATE TABLE source_files (
	username TEXT, 
	-- taargus_
	filename TEXT, 
	-- 1,1_Normal.region.png
	file_path TEXT,
	-- path/to/resources/taargus_/
	file_size_in_bytes INTEGER,
	-- 2112
	image_modified_date NUMERIC, 
	-- modified
	UNIQUE (username, filename) ON CONFLICT REPLACE
);
