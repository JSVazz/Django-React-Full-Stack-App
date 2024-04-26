import React from "react";
import "../styles/Quote.css"

function Quote({ quote, onDelete }) {
    const formattedDate = new Date(quote.created_at).toLocaleDateString("en-US");

    // Use optional chaining to safely access nested properties
    return (
        <div className="quote-container">
            <p className="quote-title">{quote.title}</p>
            <p className="quote-content">{quote.content}</p>
            {quote.author && <p className="quote-author">Author: {quote.author}</p>}
            {quote.source?.text && (
                <>
                    <p className="quote-source">Source: {quote.source.text}</p>
                    <p className="quote-source-type">Type: {quote.source.media}</p>
                    <p className="quote-source-date">Date: {quote.source.date}</p>
                </>
            )}
            {quote.category?.title && (
                <>
                    <p className="quote-category-title">Category: {quote.category.title}</p>
                    <p className="quote-category-description">{quote.category.description}</p>
                </>
            )}
            {quote.audio && (
                <audio controls>
                    <source src={quote.audio} type="audio/mpeg" />
                    Your browser does not support the audio element.
                </audio>
            )}
            <p className="quote-date">Created on: {formattedDate}</p>
            <button className="delete-button" onClick={() => onDelete(quote.id)}>Delete</button>
        </div>
    );
}

export default Quote;
