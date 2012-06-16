
###############################################################################
#
# FindPeopleByEmail
# Obtain a user's NSID by providing their email address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindPeopleByEmail(Choreography):

    """
    Create a new instance of the FindPeopleByEmail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/People/FindPeopleByEmail')


    def new_input_set(self):
        return FindPeopleByEmailInputSet()

    def _make_result_set(self, result, path):
        return FindPeopleByEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindPeopleByEmailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindPeopleByEmail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindPeopleByEmailInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your application API key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the FindEmail input for this choreography. ((required, string) Enter the email of the user being sought.)
        """
        def set_FindEmail(self, value):
            InputSet._set_input(self, 'FindEmail', value)


"""
A ResultSet with methods tailored to the values returned by the FindPeopleByEmail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindPeopleByEmailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response in XML from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindPeopleByEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindPeopleByEmailResultSet(response, path)
