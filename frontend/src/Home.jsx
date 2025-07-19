import { Link, useNavigate } from "react-router-dom";
import { saveToken } from "./auth";

export default function Home() {
  const navigate = useNavigate();

  const handleLogout = () => {
    saveToken("");
    navigate("/");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded shadow w-80 space-y-4">
        <h1 className="text-xl font-bold text-center">Bienvenido</h1>
        <Link
          to="/add"
          className="block bg-blue-500 text-white p-2 rounded text-center hover:bg-blue-600"
        >
          Añadir libro
        </Link>
        <Link
          to="/books"
          className="block bg-green-500 text-white p-2 rounded text-center hover:bg-green-600"
        >
          Ver mi biblioteca
        </Link>
        <Link
          to="/profile"
          className="block bg-yellow-500 text-white p-2 rounded text-center hover:bg-yellow-600"
        >
          Editar usuario
        </Link>
        <button
          onClick={handleLogout}
          className="w-full bg-red-500 text-white p-2 rounded hover:bg-red-600"
        >
          Cerrar sesión
        </button>
      </div>
    </div>
  );
}