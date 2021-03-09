import React from 'react';
import Spinner from 'react-spinkit';
import './LoadingIndicator.css';

function LoadingIndicator(props) {
    return (
        <div className='loadingIndicator'>
            <h3>{props.msg}</h3>
            <Spinner name='three-bounce' fadeIn='none' />
        </div>
    );
}

export default LoadingIndicator;