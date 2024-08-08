import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import YoutubeData from './YoutubeData';
import './styles.css';

const App: React.FC = () => {
    const [searchResults, setSearchResults] = useState<IYoutubeData[]>([]);
    const [keyword, setKeyword] = useState('');

    const handleSearch = async (event: React.FormEvent) => {
        event.preventDefault();
        
        const response = await fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ keyword })
        });
        const data = await response.json();
        setSearchResults(data);
    };

    return (
        <div>
            <h1>YouTube Search Page</h1>
            <form onSubmit={handleSearch} id="search-form">
                <input 
                    type="text" 
                    id="keyword" 
                    name="keyword" 
                    placeholder="Enter keyword" 
                    value={keyword}
                    onChange={(e) => setKeyword(e.target.value)}
                />
                <button type="submit">Search</button>
            </form>
            <div id="results">
                {searchResults.map((youtubeData) => (
                    <YoutubeData key={youtubeData.ykey} youtubeData={youtubeData} />
                ))}
            </div>
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));