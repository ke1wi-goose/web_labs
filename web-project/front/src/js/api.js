import axios from "axios";

const BASE_URL = "http://0.0.0.0:8000";

const apiClient = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const fetchUsers = async () => {
  try {
    const response = await apiClient.get("/users");
    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error;
  }
};

export default BASE_URL;
