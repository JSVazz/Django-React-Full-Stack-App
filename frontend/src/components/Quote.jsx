import React from "react";
import "../styles/Quote.css"

function Quote({ quote, onDelete }) {
    const formattedDate = new Date(quote.created_at).toLocaleDateString("en-US")

    return (
        <div className="quote-container">
            <p className="quote-title">{quote.title}</p>
            <p className="quote-content">{quote.content}</p>
            <p className="quote-date">{formattedDate}</p>
            <button className="delete-button" onClick={() => onDelete(quote.id)}>
                Delete
            </button>
        </div>
    );
}

export default Quote
