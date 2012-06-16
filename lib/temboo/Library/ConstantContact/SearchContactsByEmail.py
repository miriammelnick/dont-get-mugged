
###############################################################################
#
# SearchContactsByEmail
# Allows you to search Constant Contact by email to retrieve a contact's information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchContactsByEmail(Choreography):

    """
    Create a new instance of the SearchContactsByEmail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/SearchContactsByEmail')


    def new_input_set(self):
        return SearchContactsByEmailInputSet()

    def _make_result_set(self, result, path):
        return SearchContactsByEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchContactsByEmailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchContactsByEmail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchContactsByEmailInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) API Key provided by Constant Contact)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EmailAddress input for this choreography. ((string) The email address to use in your search)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Constant Contact password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserName input for this choreography. ((string) Your Constant Contact username)
        """
        def set_UserName(self, value):
            InputSet._set_input(self, 'UserName', value)


"""
A ResultSet with methods tailored to the values returned by the SearchContactsByEmail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchContactsByEmailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Constant Contact)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchContactsByEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchContactsByEmailResultSet(response, path)
