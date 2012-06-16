
###############################################################################
#
# GetAccountActivity
# Returns account transactions from a specified start date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAccountActivity(Choreography):

    """
    Create a new instance of the GetAccountActivity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/FPS/GetAccountActivity')


    def new_input_set(self):
        return GetAccountActivityInputSet()

    def _make_result_set(self, result, path):
        return GetAccountActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountActivityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAccountActivity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAccountActivityInputSet(InputSet):
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
        Set the value of the Endpoint input for this choreography. ((optional, string) The endpoint should be fps.sandbox.amazonaws.com when accessing the sandbox. Defaults to production setting:  fps.amazonaws.com.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the StartDate input for this choreography. ((required, date) The first date of transactions to return (epoch timestamp in milliseconds or formatted like 2009-10-07Z).)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)


"""
A ResultSet with methods tailored to the values returned by the GetAccountActivity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAccountActivityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAccountActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountActivityResultSet(response, path)
