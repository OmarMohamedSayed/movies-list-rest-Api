import React from 'react'
import { List, Header, Rating } from 'semantic-ui-react'

function Movies({movies}) {
    return (
        
        <List>
            {movies.map(movie => {
                return (
                    <List.Item key={ movie.title }>
                        <Header >{movie.title} <span style={{ cursor: 'pointer', paddingLeft: 20 }} onClick={async () => {
                            const movie_id = movie.id 
                            
                            const response = await fetch('/movies/'+ movie_id, {
                            method: 'DELETE'
                            
                            })
                            if (response.ok) {
                                window.location.reload(true);
                                
                            }
                        }}>&#10006;</span></Header>
                        <Rating rating={movie.rating} maxRating={ 5 } disabled/>
                    </List.Item>
            );

        })}
        </List>
    );
}

export default Movies
