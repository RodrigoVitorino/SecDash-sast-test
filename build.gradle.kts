plugins {
    kotlin("jvm") version "1.9.22"
    application
}

group = "com.example"
version = "1.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib")
}

application {
    mainClass.set("MainKt")
}
