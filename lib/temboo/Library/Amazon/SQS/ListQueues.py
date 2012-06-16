
###############################################################################
#
# ListQueues
# Returns a list of your queues.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListQueues(Choreography):

    """
    Create a new instance of the ListQueues Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/ListQueues')


    def new_input_set(self):
        return ListQueuesInputSet()

    def _make_result_set(self, result, path):
        return ListQueuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListQueuesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListQueues
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListQueuesInputSet(InputSet):
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
        Set the value of the QueueNamePrefix input for this choreography. ((optional, string) A string used to filter the list of queues.)
        """
        def set_QueueNamePrefix(self, value):
            InputSet._set_input(self, 'QueueNamePrefix', value)


"""
A ResultSet with methods tailored to the values returned by the ListQueues choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListQueuesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListQueuesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListQueuesResultSet(response, path)
