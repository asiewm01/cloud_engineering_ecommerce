import { useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  useEffect(() => {
    axios.post('http://localhost:8000/api/logout/', {}, {
      withCredentials: true
    }).then(() => {
      alert('Logged out.');
      navigate('/login');
    }).catch(err => {
      console.error("Logout failed", err);
    });
  }, [navigate]);

  return null; // no visible component
};

export default Logout;
