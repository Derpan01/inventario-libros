import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { getToken } from "./auth";

export default function AddBook() {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [edition, setEdition] = useState("");
  const [cover, setCover] = useState("paperback");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("https://inventario-libros.onrender.com/api/books/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + getToken(),
      },
      body: JSON.stringify({ title, author, edition, cover }),
    })
      .then((res) => res.json())
      .then(() => navigate("/books"))
      .catch(console.error);
  };

  return (
    <div className="p-6 max-w-md mx-auto">
      <h1 className="text-xl font-bold mb-4">Add New Book</h1>
      <form onSubmit={handleSubmit} className="space-y-3">
        <input
          type="text"
          placeholder="Title"
          className="w-full p-2 border rounded"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          type="text"
          placeholder="Author"
          className="w-full p-2 border rounded"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
        />
        <input
          type="text"
          placeholder="Edition"
          className="w-full p-2 border rounded"
          value={edition}
          onChange={(e) => setEdition(e.target.value)}
        />
        <select
          value={cover}
          onChange={(e) => setCover(e.target.value)}
          className="w-full p-2 border rounded"
        >
          <option value="paperback">Paperback</option>
          <option value="hardcover">Hardcover</option>
        </select>
        <button
          type="submit"
          className="bg-green-600 text-white p-2 w-full rounded hover:bg-green-700"
        >
          Save Book
        </button>
      </form>
    </div>
  );
}