
###############################################################################
#
# GetListOfPeople
# Retrieve a list of people in a given photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetListOfPeople(Choreography):

    """
    Create a new instance of the GetListOfPeople Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/People/GetListOfPeople')


    def new_input_set(self):
        return GetListOfPeopleInputSet()

    def _make_result_set(self, result, path):
        return GetListOfPeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListOfPeopleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetListOfPeople
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListOfPeopleInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your application API key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the PhotoID input for this choreography. ((required, string) Enter the ID of a photo for which people will be listed.)
        """
        def set_PhotoID(self, value):
            InputSet._set_input(self, 'PhotoID', value)


"""
A ResultSet with methods tailored to the values returned by the GetListOfPeople choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListOfPeopleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response in XML from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListOfPeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListOfPeopleResultSet(response, path)
