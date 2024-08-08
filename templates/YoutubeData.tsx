import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

interface IYoutubeData {
    url: string;
    title: string;
    ykey: string;
}

interface IYoutubeDataProps {
    youtubeData: IYoutubeData;
}

const YoutubeData: React.FC<IYoutubeDataProps> = ({ youtubeData }) => {
    const videoId = youtubeData.url.split('v=')[1].split('&')[0];
    const embedUrl = `https://www.youtube.com/embed/${videoId}`;

    return (
        <div className="youtubeDataContainer">
            <Link
                target="_blank"
                to={youtubeData.url}
                key={youtubeData.ykey}
                className="link"
            >
                <iframe
                    title={youtubeData.title}
                    src={embedUrl}
                    allowFullScreen
                    className="youtubeData"
                />
                <div className="youtubeTitle">{youtubeData.title}</div>
            </Link>
        </div>
    );
};

export default YoutubeData;