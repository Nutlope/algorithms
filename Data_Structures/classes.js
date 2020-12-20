// What are data structures?
// Values, relationships between them, and funcs that can be applied to the data

class Student {
  constructor(firstName, lastName, year) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.year = year;
    this.late = 0;
    this.scores = [];
  }

  // These are called instance methods
  fullName() {
    return `Your first name is ${this.firstName} ${this.lastName}`;
  }

  markLate() {
    this.late += 1;
    if (this.late >= 3) return "You're expelled!!!";
    return `${this.firstName} ${this.lastName} has been late ${this.late}`;
  }

  addScore(score) {
    this.scores.push(score);
    return this.scores;
  }

  calculateAverage() {
    let sum = this.scores.reduce((a, b) => a + b);
    return sum / this.scores.length;
  }

  // Can also define class methods, basically a utility function that doesn't
  // Depend on a specific instance

  static EnrollStudents() {
    return "ENROLLING STUDENTS FAM";
  }
}

let firstStudent = new Student("Colt", "Steele", 4);

firstStudent.addScore(68);
firstStudent.addScore(85);
console.log(firstStudent.addScore(88));
console.log(firstStudent.calculateAverage());

console.log(Student.EnrollStudents());
