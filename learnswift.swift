import Foundation

struct Person: Hashable{
  var name: String
  var age: Int
  
  init(name: String, age: Int) {
    self.name = name
    self.age = age
  }
}

let my = Person(name: "John", age: 30)
let other = Person(name: "Bob", age: 25)

print("my.name = \(my.name)")
print("my.age = \(my.age)")
print("other.name = \(other.name)")
print("other.age = \(other.age)")
