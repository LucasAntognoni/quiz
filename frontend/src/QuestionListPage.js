import React, { Component } from 'react'
import {
  QueryRenderer,
  graphql
} from 'react-relay'
import environment from './Environment'
import QuestionList from './QuestionList'

const QuestionListPageQuery = graphql`
    query QuestionListPageQuery {
        viewer {
        ...QuestionList_viewer
        }
    }
  `

class QuestionListPage extends Component {

    render() {
        return (
        <QueryRenderer
            environment={environment}
            query={QuestionListPageQuery}
            render={({error, props}) => {
            if (error) {
                return <div>{error.message}</div>
            } else if (props) {
                return <QuestionList viewer={props.viewer} />
            }
            return <div>Loading...</div>
            }}
        />
        )
    }

}
  
export default QuestionListPage