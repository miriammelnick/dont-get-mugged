
###############################################################################
#
# ReceiveMessage
# Returns one or more messages from the specified queue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ReceiveMessage(Choreography):

    """
    Create a new instance of the ReceiveMessage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/ReceiveMessage')


    def new_input_set(self):
        return ReceiveMessageInputSet()

    def _make_result_set(self, result, path):
        return ReceiveMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReceiveMessageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ReceiveMessage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ReceiveMessageInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSAccountId input for this choreography. ((required, integer) The id for the AWS account associated with the queue you're retrieving a message from (remove all dashes in the account number).)
        """
        def set_AWSAccountId(self, value):
            InputSet._set_input(self, 'AWSAccountId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the AttributeName input for this choreography. ((optional, string) The attribute you to return. Values are: All (default), SenderId, SentTimestamp, ApproximateReceiveCount, or ApproximateFirstReceiveTimestamp.)
        """
        def set_AttributeName(self, value):
            InputSet._set_input(self, 'AttributeName', value)

        """
        Set the value of the MaxNumberOfMessages input for this choreography. ((optional, integer) The maximum number of messages to return. Defaults to 1.)
        """
        def set_MaxNumberOfMessages(self, value):
            InputSet._set_input(self, 'MaxNumberOfMessages', value)

        """
        Set the value of the QueueName input for this choreography. ((required, string) The name of the queue you want to retrieve a message from.)
        """
        def set_QueueName(self, value):
            InputSet._set_input(self, 'QueueName', value)

        """
        Set the value of the VisibilityTimeout input for this choreography. ((optional, integer) The duration (in seconds) that the received messages are hidden from future retrieve requests after a ReceiveMessage request (max is 43200).)
        """
        def set_VisibilityTimeout(self, value):
            InputSet._set_input(self, 'VisibilityTimeout', value)


"""
A ResultSet with methods tailored to the values returned by the ReceiveMessage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ReceiveMessageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ReceiveMessageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReceiveMessageResultSet(response, path)
