
###############################################################################
#
# SearchContactsByUpdatedSince
# Searches your Constant Contact list by last updated date.  Use this Choreo for synchronizing your lists with other systems. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchContactsByUpdatedSince(Choreography):

    """
    Create a new instance of the SearchContactsByUpdatedSince Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/SearchContactsByUpdatedSince')


    def new_input_set(self):
        return SearchContactsByUpdatedSinceInputSet()

    def _make_result_set(self, result, path):
        return SearchContactsByUpdatedSinceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchContactsByUpdatedSinceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchContactsByUpdatedSince
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchContactsByUpdatedSinceInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) API Key provided by Constant Contact)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ListType input for this choreography. ((optional, string) The list type to query.  Supported values for this parameter are: active, removed and do-not-mail. Defaults to 'active'.)
        """
        def set_ListType(self, value):
            InputSet._set_input(self, 'ListType', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Constant Contact password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UpdatedSince input for this choreography. ((date) Epoch timestamp in milliseconds or formatted like 2009-12-01T01:00:00.000Z. Used to query for modified records.)
        """
        def set_UpdatedSince(self, value):
            InputSet._set_input(self, 'UpdatedSince', value)

        """
        Set the value of the UserName input for this choreography. ((string) Your Constant Contact username)
        """
        def set_UserName(self, value):
            InputSet._set_input(self, 'UserName', value)


"""
A ResultSet with methods tailored to the values returned by the SearchContactsByUpdatedSince choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchContactsByUpdatedSinceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Constant Contact)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchContactsByUpdatedSinceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchContactsByUpdatedSinceResultSet(response, path)
