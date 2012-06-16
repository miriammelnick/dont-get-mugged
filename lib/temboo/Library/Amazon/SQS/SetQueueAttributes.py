
###############################################################################
#
# SetQueueAttributes
# Sets an attribute of a specified queue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SetQueueAttributes(Choreography):

    """
    Create a new instance of the SetQueueAttributes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/SetQueueAttributes')


    def new_input_set(self):
        return SetQueueAttributesInputSet()

    def _make_result_set(self, result, path):
        return SetQueueAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetQueueAttributesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SetQueueAttributes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SetQueueAttributesInputSet(InputSet):
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
        Set the value of the AttributeName input for this choreography. ((required, string) The name of the attribute that you want to set. Valid values are: VisibilityTimeout, Policy, MaximumMessageSize, or MessageRetentionPeriod.)
        """
        def set_AttributeName(self, value):
            InputSet._set_input(self, 'AttributeName', value)

        """
        Set the value of the AttributeValue input for this choreography. ((required, string) The value of the attribute you want to set. Corresponds to the AttributeName you specify.)
        """
        def set_AttributeValue(self, value):
            InputSet._set_input(self, 'AttributeValue', value)

        """
        Set the value of the QueueName input for this choreography. ((required, string) The name of the queue you want to set attributes for.)
        """
        def set_QueueName(self, value):
            InputSet._set_input(self, 'QueueName', value)


"""
A ResultSet with methods tailored to the values returned by the SetQueueAttributes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SetQueueAttributesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SetQueueAttributesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetQueueAttributesResultSet(response, path)
