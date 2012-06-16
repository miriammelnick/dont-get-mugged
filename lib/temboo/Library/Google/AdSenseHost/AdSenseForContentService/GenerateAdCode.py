
###############################################################################
#
# GenerateAdCode
# Generates the ad code snippet that can be dropped into an HTML page for the page to start receiving Google Ads.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GenerateAdCode(Choreography):

    """
    Create a new instance of the GenerateAdCode Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AdSenseForContentService/GenerateAdCode')


    def new_input_set(self):
        return GenerateAdCodeInputSet()

    def _make_result_set(self, result, path):
        return GenerateAdCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GenerateAdCodeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GenerateAdCode
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GenerateAdCodeInputSet(InputSet):
        """
        Set the value of the AdStyleBackgroundColor input for this choreography. ((required, string) The background color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_AdStyleBackgroundColor(self, value):
            InputSet._set_input(self, 'AdStyleBackgroundColor', value)

        """
        Set the value of the AdStyleBorderColor input for this choreography. ((required, string) The border color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_AdStyleBorderColor(self, value):
            InputSet._set_input(self, 'AdStyleBorderColor', value)

        """
        Set the value of the AdStyleName input for this choreography. ((required, string) The ad style name.)
        """
        def set_AdStyleName(self, value):
            InputSet._set_input(self, 'AdStyleName', value)

        """
        Set the value of the AdStyleTextColor input for this choreography. ((required, string) The text color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_AdStyleTextColor(self, value):
            InputSet._set_input(self, 'AdStyleTextColor', value)

        """
        Set the value of the AdStyleTitleColor input for this choreography. ((required, string) The title color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_AdStyleTitleColor(self, value):
            InputSet._set_input(self, 'AdStyleTitleColor', value)

        """
        Set the value of the AdStyleURLColor input for this choreography. ((required, string) The URL color of this style represented as a 6-digit hexadecimal string with leading # sign.)
        """
        def set_AdStyleURLColor(self, value):
            InputSet._set_input(self, 'AdStyleURLColor', value)

        """
        Set the value of the AdUnitType input for this choreography. ((required, string) The type of ad unit or link unit. One of 'TextOnly', 'ImageOnly', 'TextAndImage', 'FourLinkUnit', or 'FiveLinkUnit'.)
        """
        def set_AdUnitType(self, value):
            InputSet._set_input(self, 'AdUnitType', value)

        """
        Set the value of the Alternate input for this choreography. ((required, string) The alternate content used to replace public service ads; either a hex color or a URL to another ad. This is usually nil.)
        """
        def set_Alternate(self, value):
            InputSet._set_input(self, 'Alternate', value)

        """
        Set the value of the ChannelName input for this choreography. ((required, string) The channel that should be used to track statistics for this page.)
        """
        def set_ChannelName(self, value):
            InputSet._set_input(self, 'ChannelName', value)

        """
        Set the value of the ClientID input for this choreography. ((required, string) The ID of the publisher to generate ad code for.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the CornerStyles input for this choreography. ((required, string) One of  'DEFAULT', 'SQUARE_CORNERS', 'SLIGHTLY_ROUNDED_CORNERS', or 'VERY_ROUNDED_CORNERS'.)
        """
        def set_CornerStyles(self, value):
            InputSet._set_input(self, 'CornerStyles', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the HostChannelName input for this choreography. ((optional, string) List of AFC host channels that should be used to track statistics for this ad code. Defaults to 'nil' indicating no host channels.)
        """
        def set_HostChannelName(self, value):
            InputSet._set_input(self, 'HostChannelName', value)

        """
        Set the value of the IsFramedPage input for this choreography. ((optional, boolean) Set to 1 if the ad code snippet will be placed within a frame in a page. Defaults to 0 (false).)
        """
        def set_IsFramedPage(self, value):
            InputSet._set_input(self, 'IsFramedPage', value)

        """
        Set the value of the Layout input for this choreography. ((required, string) The layout of the ad, e.g. '728x90'.)
        """
        def set_Layout(self, value):
            InputSet._set_input(self, 'Layout', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SynServiceID input for this choreography. ((required, string) Tthe syndication service ID.)
        """
        def set_SynServiceID(self, value):
            InputSet._set_input(self, 'SynServiceID', value)


"""
A ResultSet with methods tailored to the values returned by the GenerateAdCode choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GenerateAdCodeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GenerateAdCodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GenerateAdCodeResultSet(response, path)
