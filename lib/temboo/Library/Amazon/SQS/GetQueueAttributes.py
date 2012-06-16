
###############################################################################
#
# GetQueueAttributes
# Retrieves one or all attributes of a queue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetQueueAttributes(Choreography):

    """
    Create a new instance of the GetQueueAttributes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/GetQueueAttributes')


    def new_input_set(self):
        return GetQueueAttributesInputSet()

    def _make_result_set(self, result, path):
        return GetQueueAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetQueueAttributesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetQueueAttributes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetQueueAttributesInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSAccountId input for this choreography. ((required, integer) The AWS account number of the queue owner. Enter account number omitting any dashes.)
        """
        def set_AWSAccountId(self, value):
            InputSet._set_input(self, 'AWSAccountId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the AttributeName input for this choreography. ((optional, string) The name of the attribute that you want to retrieve for the specified queue. Defaults to 'All'.)
        """
        def set_AttributeName(self, value):
            InputSet._set_input(self, 'AttributeName', value)

        """
        Set the value of the QueueName input for this choreography. ((required, string) The name of the queue to retrieve attributes for.)
        """
        def set_QueueName(self, value):
            InputSet._set_input(self, 'QueueName', value)


"""
A ResultSet with methods tailored to the values returned by the GetQueueAttributes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetQueueAttributesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetQueueAttributesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetQueueAttributesResultSet(response, path)
