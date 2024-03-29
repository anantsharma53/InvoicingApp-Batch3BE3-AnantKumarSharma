import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import Navbar from '../NavBar/Navbar'
import './InvoiceForm.css'
import jwtDecode from 'jwt-decode';
export default function InvoiceForm() {
  const [newInvoice, setNewInvoice] = useState({})
  const [user_Id, setUserId] = useState(null);
  const navigate = useNavigate()

  useEffect(() => {
    const token = localStorage.getItem('token')
    // console.log(token);
    if (token) {
      try {
        const decodedToken = jwtDecode(token);
        if (decodedToken && decodedToken.user_id) {
          // console.log(decodedToken.user_id)
          setUserId(decodedToken.user_id); // Set the user_id in the separate state
        }
      } catch (error) {
        // Handle any error that occurs during token decoding, if necessary
      }
    }
  }, []);

  function handleSubmit() {
    const invoiceData = { ...newInvoice, user: user_Id };
    // console.log(invoiceData);
    invoiceData.items = [];
    fetch('http://127.0.0.1:8000/api/invoices/new/', {
      method: 'POST',
      body: JSON.stringify(invoiceData),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((res) => navigate('/'))
  }

  return (
    <div className="container">
      <Navbar />
      <div className="mb-3">
        <label hmlFor="name" className="form-label">
          Client Name
        </label>
        <input
          type="text"
          className="form-control"
          id="name"
          value={newInvoice.client_name}
          onInput={(e) => {
            setNewInvoice({ ...newInvoice, client_name: e.target.value })
          }}
        ></input>
      </div>
      <div className="mb-3">
        <label hmlFor="date" className="form-label">
          Date
        </label>
        <input
          type="date"
          className="form-control"
          id="date"
          value={newInvoice.date}
          onInput={(e) => {
            setNewInvoice({
              ...newInvoice,
              date: e.target.value,
            })
          }}
        ></input>
      </div>

      <button className="btn btn-primary" type="button" onClick={handleSubmit}>
        Create Invoice
      </button>
    </div>
  )
}
