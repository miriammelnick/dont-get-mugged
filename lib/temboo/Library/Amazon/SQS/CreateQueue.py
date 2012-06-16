
###############################################################################
#
# CreateQueue
# Creates a new queue with a specified queue name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateQueue(Choreography):

    """
    Create a new instance of the CreateQueue Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/CreateQueue')


    def new_input_set(self):
        return CreateQueueInputSet()

    def _make_result_set(self, result, path):
        return CreateQueueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateQueueChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateQueue
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateQueueInputSet(InputSet):
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
        Set the value of the DefaultVisibilityTimeout input for this choreography. ((optional, integer) The visibility timeout (in seconds) to use for the newly created queue.)
        """
        def set_DefaultVisibilityTimeout(self, value):
            InputSet._set_input(self, 'DefaultVisibilityTimeout', value)

        """
        Set the value of the QueueName input for this choreography. ((required, string) The name of the queue you want to create.)
        """
        def set_QueueName(self, value):
            InputSet._set_input(self, 'QueueName', value)


"""
A ResultSet with methods tailored to the values returned by the CreateQueue choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateQueueResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateQueueChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateQueueResultSet(response, path)
