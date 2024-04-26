import { useState, useEffect } from "react";
import api from "../api";
import Quote from "../components/Quote"
import "../styles/Home.css"

function Home() {
    const [quotes, setQuotes] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");

    useEffect(() => {
        getQuotes();
    }, []);

    const getQuotes = () => {
        api
            .get("/api/quotes/")
            .then((res) => res.data)
            .then((data) => {
                setQuotes(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    const deleteQuote = (id) => {
        api
            .delete(`/api/quotes/delete/${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Quote deleted!");
                else alert("Failed to delete quote.");
                getQuotes();
            })
            .catch((error) => alert(error));
    };

    const createQuote = (e) => {
        e.preventDefault();
        api
            .post("/api/quotes/", { content, title })
            .then((res) => {
                if (res.status === 201) alert("Quote created!");
                else alert("Failed to make Quote.");
                getQuotes();
            })
            .catch((err) => alert(err));
    };

    return (
        <div>
            <div>
                <h2>Quotes</h2>
                {quotes.map((quote) => (
                    <Quote quote={quote} onDelete={deleteQuote} key={quote.id} />
                ))}
            </div>
            <h2>Create a Quote</h2>
            <form onSubmit={createQuote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    );
}

export default Home;
