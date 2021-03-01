<?xml version = "1.0" encoding = "UTF-8"?>
<!-- xsl stylesheet declaration with xsl namespace: -->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="//data">
        <html>
            <head>
                <link href="styles.css" rel="stylesheet" type="text/css" />
                <title>FISHING ITEMS</title>
            </head>
            <body>
                <div class="items-wrp">

                    <xsl:for-each select="//item">
                        <div class="item">
                            <img>
                                <xsl:attribute name="src">
                                    <xsl:value-of select="./img"/>
                                </xsl:attribute>
                            </img>
                            <div class="item-text">
                                <h2>
                                    <xsl:value-of select="./name"/>
                                </h2>
                                <p class="price">
                                    <xsl:value-of select="./price"/>
                                </p>
                            </div>
                            <p class="description">
                                <xsl:value-of select="./description"/>
                            </p>
                        </div>
                    </xsl:for-each>

                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>