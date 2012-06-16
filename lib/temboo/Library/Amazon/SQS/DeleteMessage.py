
###############################################################################
#
# DeleteMessage
# Deletes a particular message from a specified queue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteMessage(Choreography):

    """
    Create a new instance of the DeleteMessage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/DeleteMessage')


    def new_input_set(self):
        return DeleteMessageInputSet()

    def _make_result_set(self, result, path):
        return DeleteMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteMessageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteMessage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteMessageInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSAccountId input for this choreography. ((required, integer) The AWS account id associated with the queue. Enter account number omitting any dashes.)
        """
        def set_AWSAccountId(self, value):
            InputSet._set_input(self, 'AWSAccountId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the QueueName input for this choreography. ((required, string) The name of the queue that contains the message you want to delete.)
        """
        def set_QueueName(self, value):
            InputSet._set_input(self, 'QueueName', value)

        """
        Set the value of the ReceiptHandle input for this choreography. ((required, string) The receipt handle associated with the message you want to delete. This is returned in the RecieveMessage request.)
        """
        def set_ReceiptHandle(self, value):
            InputSet._set_input(self, 'ReceiptHandle', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteMessage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteMessageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteMessageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteMessageResultSet(response, path)
