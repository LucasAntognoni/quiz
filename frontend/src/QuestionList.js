import React, { Component } from 'react'
import {
    createFragmentContainer,
    graphql
} from 'react-relay'
import Question from './Question'

class QuestionList extends Component {

    render() {
        return (
            <div>
            {this.props.viewer.allQuestions.edges.map(({node}) =>
                <Question key={node.__id} question={node} />
            )}
          </div>
        )
    }
}
  
export default createFragmentContainer(QuestionList, graphql`
  fragment QuestionList_viewer on Query {
    allQuestions(last: 100) @connection(key: "QuestionList_allQuestions", filters: []) {
      edges {
        node {
          ...Question_question
        }
      }
    }
  }
`)
