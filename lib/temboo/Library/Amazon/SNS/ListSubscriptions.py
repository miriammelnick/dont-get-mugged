
###############################################################################
#
# ListSubscriptions
# Returns a list of the user's subscriptions. Each call returns a limited list of subscriptions, up to 100.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListSubscriptions(Choreography):

    """
    Create a new instance of the ListSubscriptions Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/ListSubscriptions')


    def new_input_set(self):
        return ListSubscriptionsInputSet()

    def _make_result_set(self, result, path):
        return ListSubscriptionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListSubscriptionsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListSubscriptions
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListSubscriptionsInputSet(InputSet):
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
        Set the value of the NextToken input for this choreography. ((optional, string) The token returned from a previous LIstSubscriptions request.)
        """
        def set_NextToken(self, value):
            InputSet._set_input(self, 'NextToken', value)


"""
A ResultSet with methods tailored to the values returned by the ListSubscriptions choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListSubscriptionsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListSubscriptionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListSubscriptionsResultSet(response, path)
