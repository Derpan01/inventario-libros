import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./Login";
import Register from "./Register";
import BookList from "./BookList";
import AddBook from "./AddBook";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/books" element={<BookList />} />
        <Route path="/add" element={<AddBook />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;