/*

	tables.sql

*/


--DROP TABLE IF EXISTS RecipeBox;
--DROP TABLE IF EXISTS Reddit;

CREATE TABLE IF NOT EXISTS RecipeBox(
	id 				VARCHAR(100),
	title 			TEXT,
	ingredients 	TEXT,
	instructions 	TEXT
);

CREATE TABLE IF NOT EXISTS Reddit(
	id		VARCHAR(100),
	comment TEXT
);
