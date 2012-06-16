
###############################################################################
#
# Publish
# Sends a message to a topic's subscribed endpoints.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Publish(Choreography):

    """
    Create a new instance of the Publish Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/Publish')


    def new_input_set(self):
        return PublishInputSet()

    def _make_result_set(self, result, path):
        return PublishResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PublishChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Publish
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PublishInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the MessageStructure input for this choreography. ((optional, string) Can be set to 'json' if you are providing a valid JSON object for the Message input variable.)
        """
        def set_MessageStructure(self, value):
            InputSet._set_input(self, 'MessageStructure', value)

        """
        Set the value of the Message input for this choreography. ((required, string) The text for the message you want to send to the topic.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Subject input for this choreography. ((optional, string) The "Subject" line of the message when the message is delivered to e-mail endpoints or as a JSON message.)
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)

        """
        Set the value of the TopicArn input for this choreography. ((required, string) The ARN of the topic you want to publish to.)
        """
        def set_TopicArn(self, value):
            InputSet._set_input(self, 'TopicArn', value)


"""
A ResultSet with methods tailored to the values returned by the Publish choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PublishResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PublishChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PublishResultSet(response, path)
