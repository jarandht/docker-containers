const dbName = process.env.MONGO_DATABASE || "mydatabase";
const userName = process.env.MONGO_USER || "myuser";
const password = process.env.MONGO_PASSWORD || "mypassword";

db = db.getSiblingDB(dbName); // Switch to the desired database
db.createUser({
    user: userName,
    pwd: password,
    roles: [
        { role: "readWrite", db: dbName }
    ]
});