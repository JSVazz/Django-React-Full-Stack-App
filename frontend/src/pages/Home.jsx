import { useState, useEffect } from "react";
import api from "../api";
import Quote from "../components/Quote";
import "../styles/Home.css";

function Home() {
    const [quotes, setQuotes] = useState([]);
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [author, setAuthor] = useState("");  // For author name
    const [sourceText, setSourceText] = useState("");  // For source text
    const [sourceType, setSourceType] = useState("");  // For source type
    const [categoryTitle, setCategoryTitle] = useState("");  // For category title
    const [categoryDescription, setCategoryDescription] = useState("");  // For category description
    const [audio, setAudio] = useState(null);  // For audio file

    useEffect(() => {
        getQuotes();
    }, []);

    const getQuotes = () => {
        api.get("/api/quotes/")
            .then(res => setQuotes(res.data))
            .catch(err => alert("Error fetching quotes: " + err.message));
    };

    const deleteQuote = (id) => {
        console.log("Attempting to delete quote with ID:", id); // Debug: Log the ID being deleted
        api.delete(`/api/quotes/delete/${id}/`)
            .then(() => {  // Removed 'res' since it's not being used
                alert("Quote deleted!");
                getQuotes();
            })
            .catch(error => {
                console.error("Error deleting quote:", error.response);
                alert("Failed to delete quote: " + error.message);
            });
    };
    
    

    const createQuote = (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('title', title);
        formData.append('content', content);
        formData.append('author', author);
        formData.append('sourceText', sourceText);
        formData.append('sourceType', sourceType);
        formData.append('categoryTitle', categoryTitle);
        formData.append('categoryDescription', categoryDescription);
        if (audio) {
            formData.append('audio', audio);
        }

        api.post("/api/quotes/", formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(res => {
            alert("Quote created!");
            getQuotes();
        }).catch(err => alert("Failed to create quote: " + err.message));
    };

    const handleAudioChange = (event) => {
        setAudio(event.target.files[0]);
    };

    return (
        <div>
            <h2>Quotes</h2>
            {quotes.map(quote => (
                <Quote key={quote.id} quote={quote} onDelete={deleteQuote} />
            ))}
            <h2>Create a Quote</h2>
            <form onSubmit={createQuote}>
                <label htmlFor="title">Title:</label>
                <input type="text" id="title" name="title" required value={title} onChange={e => setTitle(e.target.value)} />
                <label htmlFor="content">Content:</label>
                <textarea id="content" name="content" required value={content} onChange={e => setContent(e.target.value)}></textarea>
                <label htmlFor="author">Author:</label>
                <input type="text" id="author" name="author" required value={author} onChange={e => setAuthor(e.target.value)} />
                <label htmlFor="sourceText">Source Text:</label>
                <input type="text" id="sourceText" name="sourceText" required value={sourceText} onChange={e => setSourceText(e.target.value)} />
                <label htmlFor="sourceType">Source Type:</label>
                <input type="text" id="sourceType" name="sourceType" required value={sourceType} onChange={e => setSourceType(e.target.value)} />
                <label htmlFor="categoryTitle">Category Title:</label>
                <input type="text" id="categoryTitle" name="categoryTitle" required value={categoryTitle} onChange={e => setCategoryTitle(e.target.value)} />
                <label htmlFor="categoryDescription">Category Description:</label>
                <input type="text" id="categoryDescription" name="categoryDescription" required value={categoryDescription} onChange={e => setCategoryDescription(e.target.value)} />
                <label htmlFor="audio">Audio:</label>
                <input type="file" id="audio" name="audio" onChange={handleAudioChange} />
                <input type="submit" value="Submit" />
            </form>
        </div>
    );
}

export default Home;
