import React, { Component } from 'react'
import {
    createFragmentContainer,
    graphql
} from 'react-relay'

class Question extends Component {

    render() {
        return (
            <div>
                <div>{this.props.question.text}</div>
                {Object.keys(this.props.question.choices).map(key => (
                    <p>{key} => {this.props.summary.numbers[key]}</p>
                ))}
            </div>  
        )
    }
}

export default createFragmentContainer(Question, graphql`
  fragment Question_question on QuestionType {
    text
    choices
  }
`);