import React, { Fragment } from 'react'
import { useEffect, useState } from 'react';
import axios from 'axios';

const PrimaryLayout = () => {
    const [tree, setTree] = useState([])

    useEffect(() => {
        const getData = async() => {
          try {
            const response = await axios.get('/');
            setTree(response.data)
          } catch(err) {
            console.log(err)
          }
        }
        getData();
      }, [])

    var no_columns = 1
    var no_rows = 1
    if (tree.length > 0 && tree[0].length > 0) {
        no_columns = tree[0][tree[0].length-1][4]
        no_rows = tree.length
    }

    return (
        <div className='main-layout'
            style={{ 'gridTemplateColumns': 'repeat(' + no_columns + ', 4rem)', 'gridTemplateRows': 'repeat(' + no_rows + ', 100px)'}} >

            { tree.map((level) => <Fragment>

                { level.map(node => <button 
                    key={node[0] + ' ' + node[3] + ' ' + node[5] + ' ' + node[4] + node[2]}
                    style={{ 'gridColumnStart': node[3] + 1, 'gridColumnEnd': node[4] + 1, 'gridRow': node[5] + 1 }}
                    className='node-button'>
                        {node[0]}
                    </button>) }

            </Fragment>)}
        </div>
    )
}

export default PrimaryLayout