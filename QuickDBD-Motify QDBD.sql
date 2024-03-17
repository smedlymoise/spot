-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/SAeUb6
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "User" (
    "UserName" int   NOT NULL,
    "Email" varchar(50)   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "UserName"
     )
);

CREATE TABLE "Playlist" (
    "Playlist_Name" int   NOT NULL,
    "UserName" int   NOT NULL,
    "Artist_name" int   NOT NULL,
    "Song_title" int   NOT NULL,
    CONSTRAINT "pk_Playlist" PRIMARY KEY (
        "Playlist_Name"
     )
);

CREATE TABLE "Liked_Songs" (
    "UserName" int   NOT NULL,
    "Artist_name" int   NOT NULL,
    "Song_title" int   NOT NULL,
    "Genre" int   NOT NULL,
    "Album_title" int   NOT NULL,
    CONSTRAINT "pk_Liked_Songs" PRIMARY KEY (
        "Artist_name"
     )
);

CREATE TABLE "Genre" (
    "UserName" int   NOT NULL,
    "Artist_name" int   NOT NULL,
    "Song_title" int   NOT NULL,
    "Album_title" int   NOT NULL
);

CREATE TABLE "Album" (
    "UserName" int   NOT NULL,
    "Artist_name" int   NOT NULL,
    "Song_title" int   NOT NULL,
    "Album_title" int   NOT NULL
);

ALTER TABLE "Playlist" ADD CONSTRAINT "fk_Playlist_UserName" FOREIGN KEY("UserName")
REFERENCES "User" ("UserName");

ALTER TABLE "Liked_Songs" ADD CONSTRAINT "fk_Liked_Songs_UserName" FOREIGN KEY("UserName")
REFERENCES "User" ("UserName");

ALTER TABLE "Liked_Songs" ADD CONSTRAINT "fk_Liked_Songs_Artist_name_Song_title" FOREIGN KEY("Artist_name", "Song_title")
REFERENCES "Genre" ("Artist_name", "Song_title");

ALTER TABLE "Genre" ADD CONSTRAINT "fk_Genre_Album_title" FOREIGN KEY("Album_title")
REFERENCES "Album" ("Song_title");

