
###############################################################################
#
# UpdateList
# Updates a given list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateList(Choreography):

    """
    Create a new instance of the UpdateList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/UpdateList')


    def new_input_set(self):
        return UpdateListInputSet()

    def _make_result_set(self, result, path):
        return UpdateListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateListInputSet(InputSet):
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
        Set the value of the ListID input for this choreography. ((required, string) The id of the list to update.)
        """
        def set_ListID(self, value):
            InputSet._set_input(self, 'ListID', value)

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
A ResultSet with methods tailored to the values returned by the UpdateList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateListResultSet(response, path)
