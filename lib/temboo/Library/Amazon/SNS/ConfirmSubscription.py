
###############################################################################
#
# ConfirmSubscription
# Verifies that the endpoint owner wishes to receive messages by verifying the token sent during the Subscribe action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConfirmSubscription(Choreography):

    """
    Create a new instance of the ConfirmSubscription Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/ConfirmSubscription')


    def new_input_set(self):
        return ConfirmSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return ConfirmSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConfirmSubscriptionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConfirmSubscription
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConfirmSubscriptionInputSet(InputSet):
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
        Set the value of the AuthenticateOnUnsubscribed input for this choreography. ((optional, boolean) Indicates that you want to disable the ability to unsubscribe from the subscription without authenticating. Specify 1 to enable this flag.)
        """
        def set_AuthenticateOnUnsubscribed(self, value):
            InputSet._set_input(self, 'AuthenticateOnUnsubscribed', value)

        """
        Set the value of the Token input for this choreography. ((required, string) The short-lived token sent to an endpoint during the Subscribe action.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)

        """
        Set the value of the TopicArn input for this choreography. ((required, string) The ARN of the topic you want to confirm a subscription for.)
        """
        def set_TopicArn(self, value):
            InputSet._set_input(self, 'TopicArn', value)


"""
A ResultSet with methods tailored to the values returned by the ConfirmSubscription choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConfirmSubscriptionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ConfirmSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConfirmSubscriptionResultSet(response, path)
