DROP TABLE IF EXISTS iris_db;

CREATE TABLE iris_db (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sepal_length INT NOT NULL,
    sepal_width INT NOT NULL,
    petal_length INT NOT NULL,
    petal_width INT NOT NULL,
    type_iris TEXT NOT NULL
);