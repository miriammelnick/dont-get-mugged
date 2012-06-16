
###############################################################################
#
# AddList
# Creates a new list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddList(Choreography):

    """
    Create a new instance of the AddList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/AddList')


    def new_input_set(self):
        return AddListInputSet()

    def _make_result_set(self, result, path):
        return AddListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddListInputSet(InputSet):
        """
        Set the value of the Collaborative input for this choreography. ((optional, boolean) A flag indicating that this list can be edited by friends. Set to 1 for true. Defaults to 0 (false).)
        """
        def set_Collaborative(self, value):
            InputSet._set_input(self, 'Collaborative', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) The description of the list.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the Name input for this choreography. ((required, string) The name of the list.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the PhotoID input for this choreography. ((optional, string) The id of a photo that should be set as the list photo.)
        """
        def set_PhotoID(self, value):
            InputSet._set_input(self, 'PhotoID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the AddList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddListResultSet(response, path)
