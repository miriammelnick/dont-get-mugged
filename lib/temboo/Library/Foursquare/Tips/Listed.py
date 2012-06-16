
###############################################################################
#
# Listed
# Returns the lists that a tip appears on.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Listed(Choreography):

    """
    Create a new instance of the Listed Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Tips/Listed')


    def new_input_set(self):
        return ListedInputSet()

    def _make_result_set(self, result, path):
        return ListedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Listed
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListedInputSet(InputSet):
        """
        Set the value of the Group input for this choreography. ((optional, string) Accepted values are: created, edited, followed, friends, other. If no acting user is present, only other is supported.)
        """
        def set_Group(self, value):
            InputSet._set_input(self, 'Group', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) Your Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TipID input for this choreography. ((required, string) The id of a tip to get lists for.)
        """
        def set_TipID(self, value):
            InputSet._set_input(self, 'TipID', value)


"""
A ResultSet with methods tailored to the values returned by the Listed choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListedResultSet(response, path)
