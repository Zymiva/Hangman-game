

CREATE TABLE tWords(
	WordID INT PRIMARY KEY INDENTITY(1,1)NOT NULL, 
	Word NVARCHAR(15) NOT NULL )

INSERT INTO tWords(Word) VALUES ('seesaw')
INSERT INTO tWords(Word) VALUES ('earmuffs')
INSERT INTO tWords(Word) VALUES ('headband')
INSERT INTO tWords(Word) VALUES ('tower')
INSERT INTO tWords(Word) VALUES ('surfboard')
INSERT INTO tWords(Word) VALUES ('porcupine')
INSERT INTO tWords(Word) VALUES ('sidekick')
HH
SELECT * FROM tWords
