
###############################################################################
#
# SaveSearchResultStyle
# Adds a named search result style. If a search result style with this name is already saved, this will overwrite the style's contents.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SaveSearchResultStyle(Choreography):

    """
    Create a new instance of the SaveSearchResultStyle Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AdSenseForSearchService/SaveSearchResultStyle')


    def new_input_set(self):
        return SaveSearchResultStyleInputSet()

    def _make_result_set(self, result, path):
        return SaveSearchResultStyleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SaveSearchResultStyleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SaveSearchResultStyle
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SaveSearchResultStyleInputSet(InputSet):
        """
        Set the value of the BackgroundColor input for this choreography. ((string) The background color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_BackgroundColor(self, value):
            InputSet._set_input(self, 'BackgroundColor', value)

        """
        Set the value of the BorderColor input for this choreography. ((string) The border color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_BorderColor(self, value):
            InputSet._set_input(self, 'BorderColor', value)

        """
        Set the value of the ClientID input for this choreography. ((string) The ID of the publisher to save the search result style for.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Email input for this choreography. ((string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the FaintTextColor input for this choreography. ((string) The faint text color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_FaintTextColor(self, value):
            InputSet._set_input(self, 'FaintTextColor', value)

        """
        Set the value of the LogoBackgroundColor input for this choreography. ((string) The logo background color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_LogoBackgroundColor(self, value):
            InputSet._set_input(self, 'LogoBackgroundColor', value)

        """
        Set the value of the LogoDestURL input for this choreography. ((string) The URL of the destination when the logo is clicked in the search result.)
        """
        def set_LogoDestURL(self, value):
            InputSet._set_input(self, 'LogoDestURL', value)

        """
        Set the value of the LogoHeight input for this choreography. ((integer) The height of the logo in the search result.)
        """
        def set_LogoHeight(self, value):
            InputSet._set_input(self, 'LogoHeight', value)

        """
        Set the value of the LogoPlacement input for this choreography. ((string) One of 'Top' or 'Left'.)
        """
        def set_LogoPlacement(self, value):
            InputSet._set_input(self, 'LogoPlacement', value)

        """
        Set the value of the LogoURL input for this choreography. ((string) The URL of the logo for the search result.)
        """
        def set_LogoURL(self, value):
            InputSet._set_input(self, 'LogoURL', value)

        """
        Set the value of the LogoWidth input for this choreography. ((integer) The width of the logo in the search result.)
        """
        def set_LogoWidth(self, value):
            InputSet._set_input(self, 'LogoWidth', value)

        """
        Set the value of the Password input for this choreography. ((string) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SearchResultStyleName input for this choreography. ((string) The name of this style.)
        """
        def set_SearchResultStyleName(self, value):
            InputSet._set_input(self, 'SearchResultStyleName', value)

        """
        Set the value of the SynServiceID input for this choreography. ((string) The ID of this service.)
        """
        def set_SynServiceID(self, value):
            InputSet._set_input(self, 'SynServiceID', value)

        """
        Set the value of the TextColor input for this choreography. ((string) The text color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_TextColor(self, value):
            InputSet._set_input(self, 'TextColor', value)

        """
        Set the value of the TitleColor input for this choreography. ((string) The title color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_TitleColor(self, value):
            InputSet._set_input(self, 'TitleColor', value)

        """
        Set the value of the URLColor input for this choreography. ((string) The URL color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_URLColor(self, value):
            InputSet._set_input(self, 'URLColor', value)

        """
        Set the value of the VisitedURLColor input for this choreography. ((string) The visited URL color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_VisitedURLColor(self, value):
            InputSet._set_input(self, 'VisitedURLColor', value)


"""
A ResultSet with methods tailored to the values returned by the SaveSearchResultStyle choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SaveSearchResultStyleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SaveSearchResultStyleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SaveSearchResultStyleResultSet(response, path)
