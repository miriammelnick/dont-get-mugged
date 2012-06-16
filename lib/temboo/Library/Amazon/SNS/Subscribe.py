
###############################################################################
#
# Subscribe
# Sends the endpoint a confirmation message in preparation for subscribing an endpoint.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Subscribe(Choreography):

    """
    Create a new instance of the Subscribe Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/Subscribe')


    def new_input_set(self):
        return SubscribeInputSet()

    def _make_result_set(self, result, path):
        return SubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SubscribeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Subscribe
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SubscribeInputSet(InputSet):
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
        Set the value of the Endpoint input for this choreography. ((required, string) The endpoint that will receive the notifications. Can be an email address, URL, or the ARN of an Amazon SQS queue depending on the protocol specified.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Protocol input for this choreography. ((required, string) The protocol you want to use. Accepted values are: http, https, email, email-json, or sqs.)
        """
        def set_Protocol(self, value):
            InputSet._set_input(self, 'Protocol', value)

        """
        Set the value of the TopicArn input for this choreography. ((required, string) The ARN of the topic you want to subscribe to.)
        """
        def set_TopicArn(self, value):
            InputSet._set_input(self, 'TopicArn', value)


"""
A ResultSet with methods tailored to the values returned by the Subscribe choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SubscribeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SubscribeResultSet(response, path)
