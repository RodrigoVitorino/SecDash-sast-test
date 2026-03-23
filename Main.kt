import java.sql.DriverManager
import java.io.File

// SQL Injection intencional
fun getUser(username: String): List<String> {
    val conn = DriverManager.getConnection("jdbc:sqlite:users.db")
    val stmt = conn.createStatement()
    // Vulnerabilidade: concatenação direta de input do utilizador
    val query = "SELECT * FROM users WHERE username = '$username'"
    val rs = stmt.executeQuery(query)
    val results = mutableListOf<String>()
    while (rs.next()) results.add(rs.getString(1))
    return results
}

// Path Traversal intencional
fun readFile(path: String): String {
    return File(path).readText()
}

// Hard-coded credentials intencional
fun connectDb(): java.sql.Connection {
    return DriverManager.getConnection(
        "jdbc:mysql://localhost/mydb", 
        "admin", 
        "password123"
    )
}

fun main() {
    println(getUser("test"))
    println(readFile("/etc/passwd"))
}
