import { useEffect, useState } from "react";
import { getToken } from "./auth";
import { Link } from "react-router-dom";

export default function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/books/", {
      headers: {
        Authorization: "Bearer " + getToken(),
      },
    })
      .then((res) => res.json())
      .then(setBooks)
      .catch(console.error);
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Your Books</h1>
      <Link to="/add" className="text-blue-600 underline mb-4 inline-block">+ Add Book</Link>
      <ul className="space-y-2">
        {books.map((book) => (
          <li
            key={book.id}
            className="border p-2 rounded shadow-sm bg-white"
          >
            <div className="font-semibold">{book.title}</div>
            <div className="text-sm text-gray-600">{book.author}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}